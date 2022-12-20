const LoginBlogUser = async (req, res) => {
    const { Email, Password } = req.body;
    try {
        let Data2 = await knex('blogUser').where({ Email: Email})

        // var EmailPassword = [];
        // for (let Data of data) {
        //     EmailPassword.push(Data['Email'])
        //     EmailPassword.push(Data['Password'])
        // }
        // if (EmailPassword.includes(Email)) {
        //     if (EmailPassword.includes(Password)) {
        //         const token = generateToken(Data2[0].id)
        //         res.cookie('userToken', token)
        //         res.json({ meg: 'login successfull...', logInUser: Data2 })
        //     } else {
        //         res.json({ message: 'Wrong Password' })
        //     }
        // } else {
        //     res.json({ message: "Wrong Email" })
        // }
    } catch (error) {
        res.json({ mesg: error })
    }
}