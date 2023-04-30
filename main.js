// Imports
// coming soon...

// .env file
require("dotenv").config();

// discord.js
const {Client, Intents, GatewayIntentBits} = require('discord.js');

// Discord client & intents
const client = new Client(
  {intents:
    [
      GatewayIntentBits.Guilds,
      GatewayIntentBits.GuildMessages,
      GatewayIntentBits.MessageContent
    ]
  }
);

// Console message on boot
client.on('ready', () => {
  console.log(`Logged in as ${client.user.tag}!`);
});

client.login(process.env.TOKEN);