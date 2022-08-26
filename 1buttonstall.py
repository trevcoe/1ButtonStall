# Step 1. Add your user. Go to your files and click "This PC" "Local Disk: C" then "Users" then replace trevy with your user. Leave the quotes. Caps matter.

user = "trevy"

# Step 2. Keybinds.
# The button you want to stall with. Leave the quotes. Caps Matter.
key = "X"

# Which directional air roll you normal use. Type RollRight or RollLeft. Leave the Quotes. Caps Matter.
airRoll = "RollRight"

# If you chose RollRight, type YawLeft. If you chose RollLeft, type YawRight. Leave the quotes. Caps matter.
yaw = "YawLeft"

# Don't touch anything below this line.
with open(r'C:\Users\ '+ user +r'\Documents\My Games\Rocket League\TAGame\Config\TAInput.ini', "r") as in_file:
    buf = in_file.readlines()

with open(r'C:\Users\ '+ user +r'\Documents\My Games\Rocket League\TAGame\Config\TAInput.ini', "w") as out_file:
    stall = 'GamepadBindings=( Action="' + yaw + '",Key="XboxTypeS_' + key + '", bRequired=true )AxisSign=AxisSign_Negative, )\nGamepadBindings=( Action="'+ airRoll + '",Key="XboxTypeS_'+ key +'", bRequired=true )\nGamepadBindings=( Action="Jump",Key="XboxTypeS_' + key + '", bRequired=true )\n'
    for line in buf:
        if line == 'GamepadBindings=( Action="EditorRedo",				Key="XboxTypeS_DPad_Right" )\n':
            line = line + stall
        out_file.write(line)

# Reference code. This is how it should look in the config.

#GamepadBindings=( Action="YawLeft",Key="XboxTypeS_X", bRequired=true )AxisSign=AxisSign_Negative, )
#GamepadBindings=( Action="RollRight",Key="XboxTypeS_X", bRequired=true )
#GamepadBindings=( Action="Jump",Key="XboxTypeS_X", bRequired=true )