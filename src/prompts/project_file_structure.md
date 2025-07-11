# File structure

The Ansible Module Project structures its files as follows:

## Module-specific module utility files

Module-specific utility files are specific to a given module's functionality
and contain resources that are unlikely to be imported by other modules.

The benefit is that we can modify these without impacting other modules.
For example, when modifying a VRF module's resources, we won't accidently
impact a fabric or network module.

Module-specific files are located in the following directories, where "vrf"
is the specific module name (these names will vary based on the module).

- plugins/module_utils/vrf/enums
- plugins/module_utils/vrf/validators
- plugins/module_utils/vrf/models

## Shared module utility files

Module utility files containing shared resources should be located in the following
directories.

- plugins/module_utils/common/enums
- plugins/module_utils/common/validators
- plugins/module_utils/common/models

In your code output, preface each model, class, etc, with MARK to indicate where a given
piece of code should be saved, for example:

```markdown
    # MARK plugins/module_utils/common/enums/bgp_password_encrypt.py
```
