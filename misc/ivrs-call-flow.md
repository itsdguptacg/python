# IVRS Call Flow Map

A generic customer-service IVRS: language selection, a main menu with four branches, a shared post-task menu, and global error handling.

## 1. Overview

| Item | Value |
|---|---|
| Languages | English (1), Hindi (2), Gujarati (3) |
| Main menu options | 1 Account Info, 2 Billing, 3 Tech Support, 0 Talk to Agent |
| Max retries per input | 3 |
| No-input timeout | 5 seconds (re-prompt max 2x, then Agent) |
| Callback offer threshold | Agent wait over 5 minutes |

## 2. Main Flow

```
        +---------------------+
        |    INCOMING CALL    |
        +----------+----------+
                   |
        +----------v----------+
        |   Welcome Greeting  |
        +----------+----------+
                   |
        +----------v----------+
        |  Language Selection |
        |  1 English          |
        |  2 Hindi            |
        |  3 Gujarati         |
        +----------+----------+
                   |
        +----------v----------+
   +--->|      MAIN MENU      |
   |    |  1 Account Info     |
   |    |  2 Billing          |
   |    |  3 Tech Support     |
   |    |  0 Talk to Agent    |
   |    +--+----+----+----+---+
   |       |1   |2   |3   |0
   |       v    v    v    v
   |    [ACCOUNT][BILLING][SUPPORT][AGENT]   (see section 3)
   |       |    |    |
   |       +----+----+
   |            |
   |    +-------v--------------+
   |    |   POST-TASK MENU     |
   |    |  1 Repeat            |
   |    |  * Main Menu         |
   |    |  # End call          |
   |    +---+------------+-----+
   |        |*           |#
   +--------+      +-----v-------------+
                   |  Goodbye  >  END  |
                   +-------------------+
```

The Agent branch ends in a live conversation, so it does not return to the Post-Task Menu.

## 3. Branch Flows

### 3.1 [1] Account Info

```
   Enter customer ID
          |
          v
    Validate ID
     |        |
    OK      Fail
     |        |
     |     Retry (max 3) --- still fail ---> Agent
     v
   Read plan + balance
          |
          v
    POST-TASK MENU
```

### 3.2 [2] Billing

```
   Enter customer ID
          |
          v
    Validate ID
     |        |
    OK      Fail
     |        |
     |     Retry (max 3) --- still fail ---> Agent
     v
   Billing menu
     |1 Pay now        |2 SMS last bill
     v                 v
   Payment flow      Send SMS, confirm
     |                 |
     +--------+--------+
              |
              v
        POST-TASK MENU
```

### 3.3 [3] Tech Support

```
   Support menu
     |1 Network issue      |2 Other
     v                     v
   Log ticket            Log ticket
     |                     |
     +----------+----------+
                |
                v
        Read ticket ID
                |
                v
         POST-TASK MENU
```

### 3.4 [0] Talk to Agent

```
   Check agent availability
          |
     Available?
     |yes        |no
     v           v
   Connect     Hold music
   to agent       |
                  v
              Wait over 5 min?
              |yes         |no
              v            v
        Offer callback   Keep waiting
```

## 4. Global Rules

These apply at every input node.

| Condition | Action |
|---|---|
| No input for 5 sec | Re-prompt (max 2x), then transfer to Agent |
| Invalid key | Play "Invalid option", re-prompt (max 3x), then Agent |
| Press `9` | Repeat current prompt |
| Press `*` | Return to Main Menu |

## 5. Node Reference

| Node | Type | Description |
|---|---|---|
| Welcome Greeting | Prompt | Plays brand greeting |
| Language Selection | Input (1 digit) | Sets language for all later prompts |
| Main Menu | Input (1 digit) | Routes to one of four branches |
| Validate ID | System action | Looks up customer ID in the backend |
| Payment flow | Sub-flow | Collects payment details through a secure gateway |
| Log ticket | System action | Creates a support ticket and returns an ID |
| Post-Task Menu | Input (1 digit) | Repeat, return to Main Menu, or end the call |
| Goodbye + END | Prompt, terminal | Plays closing message and disconnects |

## 6. Assumptions

- The retry count (3x), timeout (5 sec), and callback threshold (5 min) are common conventions, not fixed standards. Adjust them to your system.
- The domain is generic. Replace the branch names to match a bank, telecom, hospital, or college helpdesk.
