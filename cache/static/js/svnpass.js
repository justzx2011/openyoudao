(function() {
        $('form').submit(function() {
                var $username = $('[name=username]');
                var $password = $('[name=password]');
                var $new_password = $('[name=new_password]');
                var $new_password_repeat = $('[name=new_password_repeat]');

                if ($username.val() == '' ||
                    $password.val() == '' ||
                    $new_password.val() == '') {
                        alert ("要填全的哟！");
                        return false;
                }

                if ($new_password.val() != $new_password_repeat.val()) {
                        alert("密码不一致，打瞌睡了吧！");
                        return false;
                }

                return true;
        });

})();