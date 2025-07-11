# Ansible VRF Module Details

This module implements the following Ansible states.

- deleted
- merged
- overridden
- query
- replaced

Each state should be implemented in a separate class with corresponding names.

- Deleted
- Merged
- Overridden
- Query
- Replaced

## Validation

This module **must** leverage Pydantic version 2 to validate:

- Playbooks
- Controller responses
- Controller payloads

## File structure

This module conforms to the Ansible Project File Structure.

- Module-specific enums, validator methods, models, and other code will be located in:
  - plugins/module_utils/vrf/enums
  - plugins/module_utils/vrf/validators
  - plugins/module_utils/vrf/models
- Shared enums, validator methods, modeuls, etc, will be located in:
  - plugins/module_utils/common/enums
  - plugins/module_utils/common/validators
  - plugins/module_utils/common/models

Preface each model, class, etc, with MARK in your output to indicate where a given piece of code should be saved, for example:

```markdown
    # MARK plugins/module_utils/common/enums/bgp_password_encrypt.py
```
