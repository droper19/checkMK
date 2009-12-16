#ifndef LogEntry_h
#define LogEntry_h

#define LOGTYPE_INFO              0
#define LOGTYPE_STATE             1
#define LOGTYPE_PROGRAM           2
#define LOGTYPE_NOTIFICATION      3
#define LOGTYPE_PASSIVECHECK      4
#define LOGTYPE_ALL          0xffff

#include "nagios.h"

struct LogEntry
{
    time_t     _time;
    unsigned   _logtype;
    char      *_msg;       // split up with binary zeroes
    unsigned   _msglen;    // size of _msg
    char      *_text;      // points into msg
    char      *_host_name; // points into msg or is 0
    char      *_svc_desc;  // points into msg or is 0
    // char      *_contact_name;   // points into msg or is 0
    host      *_host;
    service   *_service;
    contact   *_contact;
    int       _state;
    int       _state_type;
    int       _attempt;
    char      *_check_output;
    char      *_comment;

    LogEntry(char *line);
    ~LogEntry();

private:
    bool handleStatusEntry();
    bool handleNotificationEntry();
    bool handlePassiveCheckEntry();
    bool handleExternalCommandEntry();
    bool handleProgrammEntry();
    bool handleMiscEntry();
    int serviceStateToInt(char *s);
    int hostStateToInt(char *s);
    int stateTypeToInt(char *s);
    int startedStoppedToInt(char *s);
};

#endif // LogEntry_h

