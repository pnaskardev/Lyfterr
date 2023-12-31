
# Lyfterr - A Real Time Taxi app built on Django Rest Framework and React

The Real-Time Taxi Booking App is a full-stack web application built with Django Rest Framework and React.js. It provides users with a real-time platform to book taxis, track rides, and facilitate seamless communication between passengers and drivers.

## Features

- User Registration and Authentication: Users can register, log in, and authenticate themselves to access the app's features.
- Real-Time Booking: Passengers can book taxis in real-time and receive instant confirmation.
- Live Ride Tracking: Passengers can track their rides on a map in real-time, ensuring transparency and convenience.
- Notifications: Passengers and drivers receive notifications regarding booking status, ride updates, and other important information.
- Admin Dashboard: An admin dashboard provides administrators with an overview of app activities and allows them to manage users, bookings, and other app data.

## Demo

Demo coming soon

## Tech Stack

**Client:** ReactJS

**Server:** Django Rest-Framework, PostgreSQL, Redis, WebSocket, Google Maps API

## Installation

1. Clone this repository using

   ```
   git clone 
   ```

2. Navigate to the backend folder,install the required dependencies and start the webserver on port 8000

   ```
   cd ./backend/
   pip install -r requirements.txt
   python manage.py runserver
   ```

3. Navigate to the frontend folder

   ```
   cd ../frontend/
   ```

4. run npm install to install all the dependencies

```
npm install
```

5. run npm start to start the client

```
npm start
```

## With Docker

OR you can build it with docker-compose file which is included in the repository.

## Contributing

We welcome contributions from the community! If you find a bug or have a feature request, please open an issue on the repository. If you would like to contribute code, please fork the repository and submit a pull request.

See `contributing.md` for ways to get started.

Please adhere to this project's `code of conduct`.
