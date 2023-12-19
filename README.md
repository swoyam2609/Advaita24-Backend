# Advaita'24 - Backend

This FastAPI Email Sender was specifically developed for the Advaita team at IIIT Bhubaneswar. It facilitates communication and coordination by allowing users to send emails related to two essential aspects: general contact inquiries and sponsorship proposals.

### Use Cases

## Author
- Swoyam Siddharth Nayak

## Getting Started

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/fastapi-email-sender.git
   cd fastapi-email-sender
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the FastAPI application:

   ```bash
   uvicorn main:app --reload
   ```

   The application will be accessible at `http://localhost:8000`.

## Usage

### Send Email - Contact Us

```bash
curl -X POST \"http://localhost:8000/send-email/contact-us\" \
  -H \"accept: application/json\" \
  -H \"Content-Type: application/json\" \
  -d '{\"subject\":\"Example Subject\",\"message\":\"Example Message\",\"name\":\"John Doe\",\"email\":\"john@example.com\"}'
```

### Send Email - Sponsor Us

```bash
curl -X POST \"http://localhost:8000/send-email/sponsor-us\" \
  -H \"accept: application/json\" \
  -H \"Content-Type: application/json\" \
  -d '{\"company_name\":\"Example Company\",\"proposal\":\"Example Proposal\",\"contact_person\":\"Jane Doe\",\"designation\":\"CEO\",\"email\":\"jane@example.com\"}'
```

## Configuration

Configure the following variables in the `main.py` file:

- `email_user`: Your email address used for authentication.
- `email_password`: Your email password.

## Contribution

Feel free to contribute to this project by opening issues or submitting pull requests.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

For any inquiries, please contact us at [b121065@iiit-bh.ac.in](mailto:b121065@iiit-bh.ac.in).