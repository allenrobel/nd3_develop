# Task

Your task is to work with the senior developer to create an Ansible module,
written in Python 3.12 or higher. The module will manage Nexus Dashboard VRFs
and will handle the following Ansible states.

- deleted
- merged
- overridden
- query
- replaced

Each state should be impemented in a separate class with corresponding names.

- Deleted
- Merged
- Overridden
- Query
- Replaced

## Ansible State Details

Ansible states implemented by the VRF module.

### deleted

Remove the resource, if it exists. NDFC uses the DELETE HTTP method for this.

If the resource does not exist, no action is taken and the Ansible result
is updated to indicate that no changes were made (i.e. `changed` = False).

### merged

Merge the resource. NDFC uses the POST HTTP method for this.

With merged state, a resource is created if it does not exist,
or is updated if it does exist.

For idempotency, each resource, if it exists, is updated only if
its current properties differ from the properties specified in
the Ansible task.

If no resources have been created or updated, the Ansible
result is updated to indicate that no changes were made (i.e.
`changed` = False).

### overridden

Override the resource. NDFC uses DELETE and POST HTTP methods for this.

With overridden state, all resources that are not specified in the
Ansible task are removed, and the specified resources are created or
updated as specified in the Ansible task.

For idempotency, each resource is modified only if its current
properties differ from the properties specified in the Ansible
task.

If no resources have been removed, created or updated, the Ansible
result is updated to indicate that no changes were made (i.e.
`changed` = False).

### query

Query the resource. NDFC uses the GET HTTP method for this.

If the resource exists, its representation is returned to the caller.
If the resource does not exist, an empty list is returned.  A
200 response is returned in both cases.

The Ansible result in this case will always have `changed` set to False.

### replaced

Replace the resource. NDFC uses the POST and DELETE HTTP methods for this.

Replace the resource if it exists and its properties differ from
the properties specified in the Ansible task. Resources not specified
in the Ansible task are not removed or modified.

## VRF Module Description

This module will handle only VRF creation and updates.

It specifically will NOT handle VRF attachments, since this is handled in a separate module.

## Validation

This module **must** leverage Pydantic version 2 to validate:

- Playbooks
- Controller responses
- Controller payloads

## File structure

This module is structured as follows.

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
