# creatorCLI_OptionsList.py
# NOTE: BLOCKED FOR TESTING PURPOSE
node_commandList = ["npm init -y"] #, "npm i dotenv express mongoose cors bcrypt jsonwebtoken multer cloudinary", "npm i -D nodemon"

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

# Options for generating different model files
UsermodelGeneration_commandList = [
    "echo 🛠️ Creating user model file... && type nul > src\\models\\user.model.js",
    # Add more commands for generating other user-related models here
]

PostmodelGeneration_commandList = ["echo 📝 Creating post model file... && type nul > src\\models\\post.model.js",]
ProductCatalogmodelGeneration_commandList = ["echo 📦 Creating product catalog model file... && type nul > src\\models\\productCatalog.model.js",]
MessagingmodelGeneration_commandList = ["echo 📨 Creating messaging model file... && type nul > src\\models\\messaging.model.js",]
EventSchedulingmodelGeneration_commandList = ["echo 📅 Creating event scheduling model file... && type nul > src\\models\\eventScheduling.model.js",]
LocationBasedmodelGeneration_commandList = ["echo 🗺️ Creating location-based model file... && type nul > src\\models\\locationBased.model.js",]
ContentManagementmodelGeneration_commandList = ["echo 📄 Creating content management model file... && type nul > src\\models\\contentManagement.model.js",]
FinancialTransactionmodelGeneration_commandList = ["echo 💰 Creating financial transaction model file... && type nul > src\\models\\financialTransaction.model.js",]
AnalyticsmodelGeneration_commandList = ["echo 📊 Creating analytics model file... && type nul > src\\models\\analytics.model.js",]
SocialNetworkmodelGeneration_commandList = ["echo 👥 Creating social network model file... && type nul > src\\models\\socialNetwork.model.js",]
PollmodelGeneration_commandList = ["echo 📊 Creating poll model file... && type nul > src\\models\\poll.model.js",]
NotificationmodelGeneration_commandList = ["echo 📩 Creating notification model file... && type nul > src\\models\\notification.model.js",]
ProductReviewmodelGeneration_commandList = ["echo 🌟 Creating product review model file... && type nul > src\\models\\productReview.model.js",]

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