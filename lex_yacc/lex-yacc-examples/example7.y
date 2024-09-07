//------------------------------------------------------------------------------

%union {
  int   val_int;
  char* val_str;
}

//------------------------------------------------------------------------------

%token KW_HEATER
%token KW_HEAT
%token KW_TARGET
%token KW_TEMP
%token <val_int> CONST_STATE
%token <val_int> CONST_NUMBER
%token <val_str> TOK_WORD

//------------------------------------------------------------------------------

%%

commands : command | command commands;
command  : heat_switch | target_set | heater_select;

heat_switch: KW_HEAT CONST_STATE {
  if($2)
    printf("\tHeater '%s' turned on\n", heater);
  else
    printf("\tHeater '%s' turned off\n", heater);
};

target_set: KW_TARGET KW_TEMP CONST_NUMBER {
  printf("\tHeater '%s' temperature set to %d\n", heater, $3);
};

heater_select: KW_HEATER TOK_WORD {
  printf("\tSelected heater '%s'\n", $2);
  heater=$2;
} ;

%%

//------------------------------------------------------------------------------
