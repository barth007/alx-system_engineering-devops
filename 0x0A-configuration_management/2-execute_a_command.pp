#This script is use to kill a command
exec {'killmenow':
    command => 'pkill -f killmenow',
    path    => '/usr/bin:/usr/local/bin',
}
