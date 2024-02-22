# creatorCLI_OptionsList.py
node_commandList = ["npm init -y", "npm i express mongoose cors bcrypt jsonwebtoken multer cloudinary", "npm i -D nodemon"]

backend_commandList = [
    "type nul > .env",
    "type nul > index.js",
    "type nul > app.js",
    "mkdir public",
    "mkdir public\\temp",
    "mkdir src",
    "mkdir src\\db",
    "mkdir src\\models",
    "mkdir src\\utils",
    "type nul > src\\utils\\ApiResponse.js",
    "mkdir src\\middlewares",
    "mkdir src\\controllers",
    "mkdir src\\routes",
]

dirOptions = {
    "--mdl": "models",
    "--db": "db",
    "--rts": "routes",
    "--mdw": "middlewares",
    "--api": "apis",
    "--pg": "pages",
    "--tst": "test",
    "--pub": "public",
    "--tmp": "temp",
    "--utl": "utils",
    "--vw": "views",
    "--stc": "static",
    "--ctr": "controllers",
}

git_commandList = ["git init", "type nul > .gitignore", "type nul > README.md", "type nul > public\\temp\\.gitkeep"]