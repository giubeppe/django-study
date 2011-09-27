#!/bin/sh
mysql kitchensink --execute "insert into pagination_data(data) values('$1')"

