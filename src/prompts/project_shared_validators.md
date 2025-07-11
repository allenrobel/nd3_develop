# Validators

The Ansible Module Project leverages the following validator functions.

These functions are mainly used within Pydantic models, but can be used
independently from these models if needed.

## validate_ipv4_cidr_host

### Description

Validates an IPv4 CIDR address e.g. 10.1.1.1/24

### Project Location

plugins/module_utils/common/validators/ipv4_cidr_host.py

### Returns

bool

- True if value is an IPv4 CIDR-format host address.
- False otherwise.

Where: value is a string representation of CIDR-format IPv4 address.

### Usage

```python
    if validate_ipv4_cidr_host("10.1.1.1/24"):
        print("Success")
    print("Failed to validate")
```

### Raises

None

### Example inputs and corresponding return values

- value: "10.10.10.1/24"  -> True
- value: "10.10.10.81/28" -> True
- value: "10.10.10.80/28" -> False (is a network)
- value: 1                -> False (is not a string)

## validate_ipv4_host

### Description

Validates an IPv4 host address without prefix e.g. 10.1.1.1

### Project Location

plugins/module_utils/common/validators/ipv4_host.py

### Returns

bool

- True if value is an IPv4 host address without a prefix.
- False otherwise.

Where: value is a string representation an IPv4 address without a prefix.

### Usage

```python
    if validate_cidr_host("10.1.1.1"):
        print("Success")
    print("Failed to validate")
```

### Raises

None

### Example inputs and corresponding return values

- value: "10.10.10.1"     -> True
- value: "10.10.10.81/28" -> False
- value: "10.10.10.0"     -> True
- value: 1                -> False (is not a string)

## validate_ipv4_multicast_group_address

### Description

Validates an IPv4 multicast address without prefix e.g. 225.1.1.1

### Project Location

plugins/module_utils/common/validators/ipv4_multicast_group_address.py

### Returns

bool

- True if value is an IPv4 multicast group address without prefix.
- False otherwise.

Where: value is a string representation an IPv4 multicast group address without prefix.

### Usage

```python
    if validate_ipv4_multicast_group_address("225.1.1.1"):
        print("Success")
    print("Failed to validate")
```

### Raises

None

### Example inputs and corresponding return values

- value: "224.10.10.1"     -> True
- value: "224.10.10.1/24"  -> False (contains prefix)
- value: "10.10.10.81/28"  -> False
- value: "10.10.10.0"      -> False
- value: 1                 -> False (is not a string)

## validate_ipv6_cidr_host

### Description

Validates an IPv6 CIDR address e.g. 2001::1/128

### Project Location

plugins/module_utils/common/validators/ipv6_cidr_host.py

### Returns

bool

- True if value is an IPv6 CIDR-format host address.
- False otherwise.

Where: value is a string representation of CIDR-format IPv6 address.

### Usage

```python
    if validate_ipv6_cidr_host("2001::1/128"):
        print("Success")
    print("Failed to validate")
```

### Raises

None

### Example inputs and corresponding return values

- value: "2001::1/128"         -> True
- value: "2001:20:20:20::1/64" -> True
- value: "2001:20:20:20::/64"  -> False (is a network)
- value: 1                     -> False (is not a string)

## validate_ipv6_host

### Description

Validates an IPv6 host address without prefix e.g. 2001::1

### Project Location

plugins/module_utils/common/validators/ipv6_host.py

### Returns

bool

- True if value is an IPv6 host address without a prefix.
- False otherwise.

Where: value is a string representation an IPv6 address without a prefix.

### Usage

```python
    if validate_ipv6_host("10.1.1.1"):
        print("Success")
    print("Failed to validate")
```

### Raises

None

### Example inputs and corresponding return values

- value: "2001::1"            -> True
- value: "2001:20:20:20::1"   -> True
- value: "2001:20:20:20::/64" -> False (has a prefix)
- value: "10.10.10.0"         -> False (is not an IPv6 address)
- value: 1                    -> False (is not an IPv6 address)
