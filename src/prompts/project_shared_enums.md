# Shared enums

The Ansible Module Project leverages the following shared enums.

## AnsibleStates

### Description

Ansible states implemented in the Ansible Module Project.
Should be used wherever an Ansible state is specified.

### Project Location

plugins/module_utils/common/enums/ansible.py

### Values

#### deleted

Remove the resource, if it exists. NDFC uses DELETE HTTP verb for this.

If the resource does not exist, no action is taken and the Ansible
result is updated to indicate that no changes were made (i.e.
`changed` = False).

#### merged

Merge the resource. NDFC uses POST HTTP verb for this.

With merged state, a resource is created if it does not exist,
or is updated if it does exist.

For idempotency, each resource, if it exists, is updated only if
its current properties differ from the properties specified in
the Ansible task.

If no resources have been created or updated, the Ansible
result is updated to indicate that no changes were made (i.e.
`changed` = False).

#### overridden

Override the resource. NDFC uses DELETE and POST HTTP verbs for this.

With overridden state, all resources that are not specified in the
Ansible task are removed, and the specified resources are created or
updated as specified in the Ansible task.

For idempotency, each resource is modified only if its current
properties differ from the properties specified in the Ansible
task.

If no resources have been removed, created or updated, the Ansible
result is updated to indicate that no changes were made (i.e.
`changed` = False).

#### query

Query the resource. NDFC uses GET HTTP verb for this.

If the resource exists, its representation is returned to the caller.
If the resource does not exist, an empty list is returned.  A
200 response is returned in both cases.

The Ansible result in this case will always have `changed` set to False.

#### replaced

Replace the resource if it exists and its properties differ from
the properties specified in the Ansible task. NDFC uses DELETE and
POST HTTP verbs for this.  Resources not specified in the
Ansible task are not removed or modified.

## BgpPasswordEncrypt

### Description

Enumerates the possible values for BGP password encryption.
Should be used wherever a BGP Password Encryption parameter value is specified.

### Project Location

plugins/module_utils/common/enums/bgp.py

### Values

#### MDS

3

#### TYPE7

7

#### NONE

-1

## RequestVerb

### Description

HTTP request methods (verbs) used in the Ansible Module Project.
Should be used wherever an HTTP verb (e.g. GET, POST, etc) is specified.

### Project Location

plugins/module_utils/common/enums/http_requests.py

### Values

#### DELETE

DELETE

#### GET

GET

#### POST

POST

#### PUT

PUT
