// +------------------------------------------------------------------+
// |             ____ _               _        __  __ _  __           |
// |            / ___| |__   ___  ___| | __   |  \/  | |/ /           |
// |           | |   | '_ \ / _ \/ __| |/ /   | |\/| | ' /            |
// |           | |___| | | |  __/ (__|   <    | |  | | . \            |
// |            \____|_| |_|\___|\___|_|\_\___|_|  |_|_|\_\           |
// |                                                                  |
// | Copyright Mathias Kettner 2009             mk@mathias-kettner.de |
// +------------------------------------------------------------------+
// 
// This file is part of Check_MK.
// The official homepage is at http://mathias-kettner.de/check_mk.
// 
// check_mk is free software;  you can redistribute it and/or modify it
// under the  terms of the  GNU General Public License  as published by
// the Free Software Foundation in version 2.  check_mk is  distributed
// in the hope that it will be useful, but WITHOUT ANY WARRANTY;  with-
// out even the implied warranty of  MERCHANTABILITY  or  FITNESS FOR A
// PARTICULAR PURPOSE. See the  GNU General Public License for more de-
// ails.  You should have  received  a copy of the  GNU  General Public
// License along with GNU Make; see the file  COPYING.  If  not,  write
// to the Free Software Foundation, Inc., 51 Franklin St,  Fifth Floor,
// Boston, MA 02110-1301 USA.

#include "Table.h"
#include "Column.h"
#include "Query.h"
#include "logger.h"

void Table::addColumn(Column *col)
{
    // do not insert column if one with that name
    // already exists. Delete that column in that
    // case. (For example needed for TableLog->TableHosts,
    // which both define host_name.
    if (column(col->name())) {
	delete col;
	logger(LG_INFO, "HIRN: Doppelte Spalte %s kommt weg", col->name());
    }
    else
	_columns.insert(make_pair(col->name(), col));
}

bool Table::hasColumn(Column *col)
{
  // this is not very efficient but seldomly used 
   for (_columns_t::iterator it = _columns.begin();
	 it != _columns.end();
	 ++it)
   {
      if (col == it->second)
	 return true;
   }
   return false;
}



Table::~Table()
{
   for (_columns_t::iterator it = _columns.begin();
	 it != _columns.end();
	 ++it)
   {
      delete it->second;
   }
}


void Table::addAllColumnsToQuery(Query *q)
{
   for (_columns_t::iterator it = _columns.begin();
	 it != _columns.end();
	 ++it)
   {
      q->addColumn(it->second);
   }
}


Column *Table::column(const char *name)
{
   _columns_t::iterator it = _columns.find(string(name));
   if (it == _columns.end())
      return 0;
   else
      return it->second;
}

