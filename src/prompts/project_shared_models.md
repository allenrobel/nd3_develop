# Shared Pydantic Models

The Ansible Module Project leverages the following shared Pydantic models

## IPv4CidrHostModel

### Description

Validates a CIDR-format IPv4 host address.

### Project Location

plugins/module_utils/common/models/ipv4_cidr_host.py

### Raises

- ValueError: If the input is not a valid CIDR-format IPv4 host address.

### Example usage

```python
from ..common.module_utils.models.ipv4_cider_host import IPv4CidrHostModel

try:
    ipv4_cidr_host_address = IPv4CidrHostModel(ipv4_cidr_host="192.168.1.1/24")
except ValueError as error:
    # Handle the error, for example
    msg = f"Error validating {ipv4_cidr_host}. "
    msg += f"Error detail: {error}."
    raise ValueError(msg) from error
```

## IPv4HostModel

### Description

Validates an IPv4 host address without prefix

### Project Location

plugins/module_utils/common/models/ipv4_host.py

### Raises

- ValueError: If the input is not a valid IPv4 host address without prefix.

### Example usage

```python
from ..common.module_utils.models.ipv4_host import IPv4HostModel

try:
    ipv4_host_address = IPv4HostModel(ipv4_host="192.168.1.1")
except ValueError as error:
    # Handle the error, for example
    msg = f"Error validating {ipv4_host}. "
    msg += f"Error detail: {error}."
    raise ValueError(msg) from error
```

## IPv6CidrHostModel

### Description

Validates a CIDR-format IPv6 host address.

### Project Location

plugins/module_utils/common/models/ipv6_cidr_host.py

### Raises

- ValueError: If the input is not a valid CIDR-format IPv6 host address.

### Example usage

```python
from ..common.module_utils.models.ipv6_cider_host import IPv4CidrHostModel

try:
    ipv6_cidr_host_address = IPv6CidrHostModel(ipv6_cidr_host="192.168.1.1/24")
except ValueError as error:
    # Handle the error, for example
    msg = f"Error validating {ipv6_cidr_host}. "
    msg += f"Error detail: {error}."
    raise ValueError(msg) from error
```

## IPv6HostModel

### Description

Validates an IPv6 host address without prefix.

### Project Location

plugins/module_utils/common/models/ipv6_host.py

### Raises

- ValueError: If the input is not a valid IPv6 host address.

### Example usage

```python
from ..common.module_utils.models.ipv6_host import IPv6HostModel

try:
    ipv6_host_address = IPv6HostModel(ipv6_host="2001::/1")
except ValueError as error:
    # Handle the error, for example
    msg = f"Error validating {ipv6_host}. "
    msg += f"Error detail: {error}."
    raise ValueError(msg) from error
```
