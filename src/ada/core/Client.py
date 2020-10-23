#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
#    Copyright (C) 2020 Samsung Electronics. All Rights Reserved.
#       Authors: Anonymous Cat (Samsung R&D Poland)
#
#    This file is part of ADA.
#
#    ADA is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 2 of the License, or
#    (at your option) any later version.
#
#    ADA is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with ADA. If not, see <http://www.gnu.org/licenses/>.
#

import logging;
import asyncio;
import discord;
import signal;
import typing;

class Client(discord.Client):
	"""
		Class for integration with discord client library, which implements:
		* saving and executing handlers for different events,
		* sending and receiving the discord messages.
		
		The following events can be triggered:
		* ready    - Triggered when the client is ready for receiving the messages.
		* periodic - Triggered periodically every `conf_delay` seconds.
		* finish   - Triggered just before main event loop will be stopped.
		* message  - Triggered when the message is received from server.
		* format   - Triggered when response message has to be formatted.
		
		List of arguments names for each handler call:
		* handler_ready()
		* handler_periodic()
		* handler_finish()
		* handler_message(whoami, author, channel, content)
		* handler_format(content)
	"""
	
	def __init__(self,
			handler_ready    : typing.Callable[[], str] = None,
			handler_periodic : typing.Callable[[], str] = None,
			handler_finish   : typing.Callable[[], str] = None,
			handler_message  : typing.Callable[[int, int, str, str], str] = None,
			handler_format   : typing.Callable[[str], typing.List[str]]   = None,
			conf_channel     : str    = "food",
			conf_delay       : float  = 0.1,
			conf_loopback    : bool   = False,
			logger           : logging.Logger = None):
		"""
			Args:
				handler_ready:    Function or object, to be called on ready event.
				handler_periodic: Function or object, to be called on periodic event.
				handler_finish:   Function or object, to be called on finish event.
				handler_message:  Function or object, to be called on message event.
				handler_format:   Function or object, to format and split message before send.
				conf_channel:     Name of a default bot channel.
				conf_delay:       Delay between client events.
				conf_loopback:    Allow to parsing messages from yourself.
		"""
		
		# Initialize discord client
		super().__init__();
		
		# If format handler does not exists,
		# then create in place default one.
		if not handler_format:
			handler_format = lambda x: [x[:1500]] if isinstance(x, str) else [];
		
		# Save handlers for different events
		self.handler_ready    = handler_ready;
		self.handler_periodic = handler_periodic;
		self.handler_finish   = handler_finish;
		self.handler_message  = handler_message;
		self.handler_format   = handler_format;
		
		# Save client configuration
		self.conf_channel  = conf_channel;
		self.conf_delay    = conf_delay;
		self.conf_loopback = conf_loopback;
		
		# Save logger
		self.logger = logger;
	
	async def on_ready(self):
		"""
			This event is triggered, when a client is ready for receiving the
			messages from discord server. It creates a triggers for the periodic
			and finish events and finally call the ready handler.
		"""
		
		# Log information about triggered event
		self.logger.info("Ready event was triggered!");
		
		# Create a task, that will trigger the periodic event
		task = self.on_periodic();
		self.loop.create_task(task);
		
		# Add a handler, that will trigger the finish event
		handler = lambda: self.loop.create_task(self.on_finish());
		self.loop.add_signal_handler(signal.SIGHUP,  handler);
		self.loop.add_signal_handler(signal.SIGINT,  handler);
		self.loop.add_signal_handler(signal.SIGTERM, handler);
		
		# Exit this event if its handler does not exists
		if not self.handler_ready:
			return;
		
		# Execute handler for ready event
		response = self.handler_ready();
		
		# Send response returned from ready handler
		await self.send_message(response);
	
	async def on_periodic(self):
		"""
			This event is triggered periodically every `conf_delay` seconds.
		"""
		
		# Log information about triggered event
		self.logger.debug("Periodic event was triggered!");
		
		if not self.handler_periodic:
			msg = "There is no periodic event handler!";
			self.logger.warning(msg);
			return;
		
		# Handle current events
		response = self.handler_periodic();
		
		# Send response returned from periodic handler
		if response: await self.send_message(response);
		
		# Asynchronous wait for the next execution
		delay = self.conf_delay;
		await asyncio.sleep(delay);
		
		# Create a task, that will trigger this event again
		task = self.on_periodic();
		self.loop.create_task(task);
	
	async def on_finish(self):
		"""
			This event is triggered, when client is stopping.
		"""
		
		# Log information about triggered event
		self.logger.info("Finish event was triggered!");
		
		# If exists handler for this event
		if self.handler_finish:
			
			# Execute handler for finish event
			response = self.handler_finish();
			
			# Send response returned from finish handler
			await self.send_message(response);
		
		# Stop event loop
		self.loop.stop();
	
	async def on_message(self, message):
		"""
			This event is triggered, when message from discord is received.
			It is sending message information to message handler and send
			back response message to discord.
		"""
		
		# Get required informations about message
		whoami  = getattr(self.user,       "id",   None);
		author  = getattr(message.author,  "id",   None);
		channel = getattr(message.channel, "name", None);
		content = message.content;
		
		# Log information about triggered event
		self.logger.info("Message event was triggered!");
		self.logger.info(" * whoami  : %s", whoami);
		self.logger.info(" * author  : %s", author);
		self.logger.info(" * channel : %s", channel);
		self.logger.info(" * content : %s", content);
		
		# MAke sure that whoami and author exists
		if not whoami or not author:
			msg = "There is no whoami or author (%s, %s)!";
			self.logger.error(msg, whoami, author);
			return;
		
		# If loopback is disabled, then do not parse messages from yourself.
		if not self.conf_loopback and whoami == author:
			msg = "Loopback parsing is disabled (%s, %s, %s)!";
			self.logger.info(msg, self.conf_loopback, whoami, author);
			return;
		
		# Only a private or selected public channel should be parsed
		if channel and channel != self.conf_channel:
			msg = "Inappropriate channel (%s, %s)!";
			self.logger.info(msg, channel, self.conf_channel);
			return;
		
		# Cancel if there is nothing to parse
		if not content:
			msg = "There is no content (%s)!";
			self.logger.info(msg, content);
			return;
		
		# Make sure, that event handler exists
		if not self.handler_message:
			msg = "There is no message event handler!";
			self.logger.warning(msg);
			return;
		
		# Send message information to handler and save message response
		response = self.handler_message(whoami, author, channel, content);
		
		# Send response returned from message handler
		await self.send_message(response, channel, author);
	
	async def send_message(self,
			content   : str,
			channel   : str = None,
			recipient : int = None):
		"""
			Send reply to discord channel or to private conversation.
			If reply is too long it will be splitted into smaller messages.
		"""
		
		msg = "Sending a message: %s, %s, %s";
		self.logger.info(msg, recipient, channel, content);
		
		# If there is not content, then cancel sending
		if not content:
			return;
		
		# If there is channel name,
		# then send response to this channel
		if channel:
			channel_objs = self.get_all_channels();
			channel_obj  = discord.utils.get(channel_objs, name=channel);
		
		# TODO: If there is recipient user id,
		# then send response to user private channel
		elif recipient:
			user = self.get_user(recipient);
			if not user:
				msg = "User not found (%s)!";
				self.logger.warning(msg, recipient);
				return;
			if not user.dm_channel:
				await user.create_dm();
			channel_obj = user.dm_channel;
		
		# If there is no recipient and channel,
		# then send response to the default channel
		else: # not recipient and not channel:
			channel      = self.conf_channel;
			channel_objs = self.get_all_channels();
			channel_obj  = discord.utils.get(channel_objs, name=channel);
		
		# Make sure that channel object exists
		if not channel_obj:
			msg = "Channel not found (%s, %s)!";
			self.logger.warning(msg, recipient, channel);
			return;
		
		# Format and split message before sending it
		pieces = self.handler_format(content);
		
		# Send each content piece
		for piece in pieces:
			await channel_obj.send(piece);

