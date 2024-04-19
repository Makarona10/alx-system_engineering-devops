# installs the package puppet-lint

package { 'flask=2.1.0':
  ensure   => installed,
  provider => 'pip3'
}
package {'werkzeug=2.1.1':
  ensure   => installed,
  provider => 'pip3',
}

