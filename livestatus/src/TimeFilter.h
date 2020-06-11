// Copyright (C) 2019 tribe29 GmbH - License: GNU General Public License v2
// This file is part of Checkmk (https://checkmk.com). It is subject to the
// terms and conditions defined in the file COPYING, which is part of this
// source code package.

#ifndef TimeFilter_h
#define TimeFilter_h

#include "config.h"  // IWYU pragma: keep

#include <bitset>
#include <chrono>
#include <cstdint>
#include <memory>
#include <optional>
#include <string>

#include "ColumnFilter.h"
#include "Filter.h"
#include "contact_fwd.h"
#include "opids.h"
class Row;
class TimeColumn;

class TimeFilter : public ColumnFilter {
public:
    TimeFilter(Kind kind, const TimeColumn &column, RelationalOperator relOp,
               const std::string &value);

    bool accepts(Row row, const contact *auth_user,
                 std::chrono::seconds timezone_offset) const override;

    [[nodiscard]] std::optional<int32_t> greatestLowerBoundFor(
        const std::string &column_name,
        std::chrono::seconds timezone_offset) const override;

    [[nodiscard]] std::optional<int32_t> leastUpperBoundFor(
        const std::string &column_name,
        std::chrono::seconds timezone_offset) const override;

    [[nodiscard]] std::optional<std::bitset<32>> valueSetLeastUpperBoundFor(
        const std::string &column_name,
        std::chrono::seconds timezone_offset) const override;

    [[nodiscard]] std::unique_ptr<Filter> copy() const override;
    [[nodiscard]] std::unique_ptr<Filter> negate() const override;

private:
    const TimeColumn &_column;
    const int32_t _ref_value;
};

#endif  // TimeFilter_h
