#include <iostream>
#include <csignal>
#include <unistd.h>

void handler(int signum) {
    std::cout << "C++ process: *** Received signal " << signum << " ***"<< std::endl;
}

int main() {
    signal(SIGINT, handler);
    signal(SIGTERM, handler);

    int counter = 0;
    while(1) {
        std::cout << "C++ node says hello " << counter++ << std::endl;
        sleep(1.0);
    }

    return 0;
}
