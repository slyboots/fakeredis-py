INVALID_EXPIRE_MSG = "ERR invalid expire time in {}"
WRONGTYPE_MSG = "WRONGTYPE Operation against a key holding the wrong kind of value"
SYNTAX_ERROR_MSG = "ERR syntax error"
INVALID_INT_MSG = "ERR value is not an integer or out of range"
INVALID_FLOAT_MSG = "ERR value is not a valid float"
INVALID_OFFSET_MSG = "ERR offset is out of range"
INVALID_BIT_OFFSET_MSG = "ERR bit offset is not an integer or out of range"
INVALID_BIT_VALUE_MSG = "ERR bit is not an integer or out of range"
INVALID_DB_MSG = "ERR DB index is out of range"
INVALID_MIN_MAX_FLOAT_MSG = "ERR min or max is not a float"
INVALID_MIN_MAX_STR_MSG = "ERR min or max not a valid string range item"
STRING_OVERFLOW_MSG = "ERR string exceeds maximum allowed size (512MB)"
OVERFLOW_MSG = "ERR increment or decrement would overflow"
NONFINITE_MSG = "ERR increment would produce NaN or Infinity"
SCORE_NAN_MSG = "ERR resulting score is not a number (NaN)"
INVALID_SORT_FLOAT_MSG = "ERR One or more scores can't be converted into double"
SRC_DST_SAME_MSG = "ERR source and destination objects are the same"
NO_KEY_MSG = "ERR no such key"
INDEX_ERROR_MSG = "ERR index out of range"
ZADD_NX_XX_ERROR_MSG = "ERR ZADD allows either 'nx' or 'xx', not both"
ZADD_INCR_LEN_ERROR_MSG = "ERR INCR option supports a single increment-element pair"
NX_XX_GT_LT_ERROR_MSG = "ERR NX and XX, GT or LT options at the same time are not compatible"
EXPIRE_UNSUPPORTED_OPTION = "ERR Unsupported option {}"
ZUNIONSTORE_KEYS_MSG = "ERR at least 1 input key is needed for ZUNIONSTORE/ZINTERSTORE"
WRONG_ARGS_MSG = "ERR wrong number of arguments for '{}' command"
UNKNOWN_COMMAND_MSG = "ERR unknown command '{}'"
EXECABORT_MSG = "EXECABORT Transaction discarded because of previous errors."
MULTI_NESTED_MSG = "ERR MULTI calls can not be nested"
WITHOUT_MULTI_MSG = "ERR {0} without MULTI"
WATCH_INSIDE_MULTI_MSG = "ERR WATCH inside MULTI is not allowed"
NEGATIVE_KEYS_MSG = "ERR Number of keys can't be negative"
TOO_MANY_KEYS_MSG = "ERR Number of keys can't be greater than number of args"
TIMEOUT_NEGATIVE_MSG = "ERR timeout is negative"
NO_MATCHING_SCRIPT_MSG = "NOSCRIPT No matching script. Please use EVAL."
GLOBAL_VARIABLE_MSG = "ERR Script attempted to set global variables: {}"
COMMAND_IN_SCRIPT_MSG = "ERR This Redis command is not allowed from scripts"
BAD_SUBCOMMAND_MSG = "ERR Unknown {} subcommand or wrong # of args."
BAD_COMMAND_IN_PUBSUB_MSG = \
    "ERR only (P)SUBSCRIBE / (P)UNSUBSCRIBE / PING / QUIT allowed in this context"
CONNECTION_ERROR_MSG = "FakeRedis is emulating a connection error."
REQUIRES_MORE_ARGS_MSG = "ERR {} requires {} arguments or more."
LOG_INVALID_DEBUG_LEVEL_MSG = "ERR Invalid debug level."
LUA_COMMAND_ARG_MSG6 = "ERR Lua redis() command arguments must be strings or integers"
LUA_COMMAND_ARG_MSG = "ERR Lua redis lib command arguments must be strings or integers"
LUA_WRONG_NUMBER_ARGS_MSG = "ERR wrong number or type of arguments"
SCRIPT_ERROR_MSG = "ERR Error running script (call to f_{}): @user_script:?: {}"
RESTORE_KEY_EXISTS = "BUSYKEY Target key name already exists."
RESTORE_INVALID_CHECKSUM_MSG = "ERR DUMP payload version or checksum are wrong"
RESTORE_INVALID_TTL_MSG = "ERR Invalid TTL value, must be >= 0"

FLAG_NO_SCRIPT = 's'  # Command not allowed in scripts
