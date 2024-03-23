#!/usr/bin/pup
# Install ispecific version of lask (2.1.0)
package {'flask':
  ensure   => '2.1.0',
  provider => 'pip3'
}
