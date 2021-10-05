from Main.main import process_new_round_event
from Models.timeout_certificate import TimeoutCertificate


def main():
    print('Entry')
    tc = TimeoutCertificate()
    process_new_round_event(tc)


if __name__ == '__main__':
    main()
