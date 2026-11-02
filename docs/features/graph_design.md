# Graph Design

## Graph Type

Directed Bipartite Graph

---

# Node Types

Account Node

Format:

ACCT_xxxxx

Counterparty Node

Format:

CP_xxxxx

---

# Edge Definition

ACCT_xxxxx
    →
CP_xxxxx

Each transaction generates one edge.

---

# Edge Attributes

transaction_count

transaction_volume

average_amount

---

# Graph Features

in_degree

out_degree

weighted_degree

pagerank

community_size

neighbor_count

two_hop_neighbor_count

---

# Notes

account_id and counterparty_id belong to different namespaces.

Do not merge them into a single node type.