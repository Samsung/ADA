Automatic Delivery Aid: Roles
==============================

| Name         | Value | Description                                                                  |
|:------------:|------:|------------------------------------------------------------------------------|
| `DELETED`    |   -30 | The account is deleted, saldo is already settled, user is not displayed.     |
| `SETTLEMENT` |   -20 | The account is pending for the balance settlement before removing.           |
| `BANNED`     |   -10 | The account has temporary ban for all commands.                              |
| `NONE`       |     0 | This user does not register his account yet.                                 |
| `UNACCEPTED` |    10 | The account is pending for acceptance.                                       |
| `REGULAR`    |    20 | The account with regular privileges.                                         |
| `MODERATOR`  |    30 | The account with moderator privileges.                                       |
| `ADMIN`      |    40 | The account with administrator privileges.                                   |
| `ROOT`       |    50 | The account with administrator privileges and protection from role changing. |

