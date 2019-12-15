    function validateForm()
    {
        var validate = true;

        //Username
        document.getElementById('user_error').innerHTML = "";
        var user = document.getElementById('user_text').value;
        if(user != "")
        {
            if (/^.*[^\s{1,}]\s.*/.test(user) == true)
            {
                document.getElementById('user_error').innerHTML = "Username cannot contain a space";
                return false;
            }

        }
        else
        {
            document.getElementById('user_error').innerHTML = "Must be filled in";
            return false;
        }

        //Password
        document.getElementById('pass_error').innerHTML = "";
        var pass = document.getElementById('pass_text').value;
        if(pass != "")
        {
            if (/^.*[^\s{1,}]\s.*/.test(pass) == true)
            {
                document.getElementById('pass_error').innerHTML = "Password cannot contain a space";
                return false;
            }

        }
        else
        {
            document.getElementById('pass_error').innerHTML = "Must be filled in";
            return false;

        }


    }
