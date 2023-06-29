# writing a configuration file with pp

function create_configFile($host, $hostname, $user, $file_identity, $no_auth) {
    $all_content = "\nHostName ${hostname}\nUser  ${user}\nIdentityFile ${file_identity}\n${no_auth}\n"
    file { '/home/vagrant/.ssh/config':
        ensure  => present,
        content => $all_content,
  }
}

create_configFile('remote', '54.175.155.102', 'ubuntu', '~/.ssh/school', 'PasswordAuthentication no')
