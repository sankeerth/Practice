from collections import defaultdict

def build_map(domain):
    for d in domain:
        parent = d.split('.')
        domain_map[parent[-1]]
        for i in range(len(parent) - 1):
            domain_map[parent[-1]].append(parent[i])


def longest_matching_parent_domain(domain):
    domain = domain.split('.')
    parent = domain[-1]
    res = list()
    res.append(parent)

    if domain_map[parent]:
        domains = domain_map[parent]
        for p in domain[::-1]:
            print(p)
            if p == parent:
                continue
            elif p not in domains:
                res.append(p)
                break
            res.append(p)
    else:
        res.append(domain[-2])
    print(res)
    return '.'.join(res[::-1])


l = ['com', 'uk', 'co.uk', 'gov.uk', 'nhs.uk', 'org.uk']
domain_map = defaultdict(list)
build_map(l)
print(longest_matching_parent_domain('www.google.com'))
