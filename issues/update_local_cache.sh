#!/usr/bin/env bash
wget -np -k -e robots=off -r -l 1 https://github.com/Naereen/cuisine/{milestones,issues,labels}/

gh2md -t $(cat ~/.gh2md_token) Naereen/cuisine cuisine-issues.md
