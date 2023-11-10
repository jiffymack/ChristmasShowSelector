#!/bin/bash

# Define the path to the s.txt file
file_path="/home/pi/s.txt"

# Define the serial port device
serial_device="/dev/ttyUSB0"

# Baud rate for serial communication
baud_rate="9600"

# Function to send data to the serial port
send_data() {
    local data="$1"
    echo -e "$data" > "$serial_device"
}

# Function to read and print data from the serial port
read_serial() {
    while read -r line; do
        echo "Received from serial port: $line"
    done < "$serial_device"
}

# Initial timestamp to ignore changes made before script start
last_timestamp=$(date +%s)

# Start the serial data reading in the background
read_serial &

while true; do
    # Wait for file changes using inotifywait
    inotifywait -e modify "$file_path" >/dev/null 2>&1

    # Read the last line from the file
    last_line=$(tail -n 1 "$file_path")

    # Extract 'v' value and timestamp from the last line
    v=$(echo "$last_line" | awk -F ', ' '{print $1}')
    timestamp=$(echo "$last_line" | awk -F ', ' '{print $2}')

    # Convert timestamp to epoch time
    timestamp_epoch=$(date -d "$timestamp" +%s)

    # Calculate time difference in seconds
    time_diff=$((timestamp_epoch - last_timestamp))

    # Check if 'v' is greater than 0 and time difference is greater than or equal to 1 seconds
    if [[ "$v" -ge 0 && "$time_diff" -ge 1 ]]; then
        # Create the data string to send
        data=" \rr$((v + 1)) p\r"
        echo $data
        # Send the data to the serial port
        send_data "$data"

        # Update the last timestamp
        last_timestamp="$timestamp_epoch"
    fi
done

