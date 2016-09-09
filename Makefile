#
# For continuous tests:
#
# 1. Generate a new API token at http://neurovault.org/accounts/tokens/
#
# 2. Store your NEUROVAULT_ACCESS_TOKEN in .env file. Example:
#
#    NEUROVAULT_ACCESS_TOKEN=Abracadabra
#
# 3. Run
#
#    make watch
#

-include .env

watch:
	NEUROVAULT_ACCESS_TOKEN=${NEUROVAULT_ACCESS_TOKEN} ptw

.PHONY: watch
