Automatic Delivery Aid: Commands
================================

`@ada register`
`@ada help`


## States

### Sleep
### Submit
### Order
### Summary
### Adjustment


## Settings

### Restaurants

| Command                        | Description |
|--------------------------------|-------------|
| `@ada set rest-add NAME URL`   | Adds new restaurant to the database.
| `@ada set rest-del NAME`       | Removes restaurant from the database.
| `@ada set rest-url NAME URL`   | Changes the URL address of the restaurant.
| `@ada set rest-mv  NAME NAME2` | Changes the name of the restaurant.

### Timeouts

| Command                             | Description |
|-------------------------------------|-------------|
| `@ada set autostart          HH:MM` | Changes the time when the automatic transition between states `waiting` and `submit` takes place.
| `@ada set timeout-submit     HH:MM` | Changes the time when the automatic transition between states `submit` and `voting` takes place.
| `@ada set timeout-voting     HH:MM` | Changes the time when the automatic transition between states `voting` and `ordering` takes place.
| `@ada set timeout-ordering   HH:MM` | Changes the time when the automatic transition between states `ordering` and `summary` takes place.
| `@ada set timeout-summary    HH:MM` | Changes the time when the reminder of required transition between states `summary` and `adjustment` is displayed.
| `@ada set timeout-adjustment HH:MM` | Changes the time when the reminder of required transition between states `adjustment` and `waiting` is displayed.

