# This manifest modifies the limit descriptor file for a user

exec { 'change the amount of open files for the holberton user':
        command => 'sed -i \'s/^holberton hard.*$/holberton hard nofile 50000/g\' /etc/security/limits.conf',
        path => '/bin/',
}


exec { 'for soft links':
        command => 'sed -i \'s/^holberton soft.*$/holberton soft nofile 40000/g\' /etc/security/limits.conf',
        path => '/bin/',
}
