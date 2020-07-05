# Features:
- View available tickets for a movie.
- Book a ticket.
- Reserve a ticket. (For example, customer has started the checkout process).
- Register new movie details.

# Basics
- Will have a 'Show' table `show_id, name, time, cinema_id`.
- Available ticket table - `ticket_id, show_id`.
- Reserved ticket table - `ticket_id, show_id, user_id`.
- Booked ticket table - `ticket_id, show_id, user_id`.
- Sharding can be done either by city or by consistent hashing on movie id.