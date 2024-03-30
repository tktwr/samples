// *sample:cpp_lib.spdlog*
#include <iostream>
#include <spdlog/spdlog.h>

int main(int, char* [])
{
    spdlog::set_pattern("[%l] %v");

    //Multithreaded console logger(with color support)
    //auto console = spdlog::stdout_color_mt("console");
    auto console = spdlog::stdout_logger_mt("console");
    console->info("Welcome to spdlog!") ;
    console->info("An info message example {}..", 1);
    console->info("{:>53}", "[OK]");

    try 
    {
        // Create basic file logger (not rotated)
        auto my_logger = spdlog::basic_logger_mt("basic_logger", "spdlog_basic.txt");
        
        // create a file rotating logger with 5mb size max and 3 rotated files
        auto file_logger = spdlog::rotating_logger_mt("file_logger", "spdlog_rotating.txt", 1024 * 1024 * 5, 3);
    }
    catch (const spdlog::spdlog_ex& ex)
    {
        std::cout << "Log initialization failed: " << ex.what() << std::endl;
    }
}
