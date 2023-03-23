// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * parse keywords response
 */
public class ParseKeywordsResponse extends TeaModel {
    /**
     * <p>AddressLine</p>
     */
    @NameInMap("address_line")
    public String addressLine;

    @NameInMap("tags")
    public java.util.List<SystemTag> tags;

    @NameInMap("time_range")
    public ParseTimeRange timeRange;

    public static ParseKeywordsResponse build(java.util.Map<String, ?> map) throws Exception {
        ParseKeywordsResponse self = new ParseKeywordsResponse();
        return TeaModel.build(map, self);
    }

    public ParseKeywordsResponse setAddressLine(String addressLine) {
        this.addressLine = addressLine;
        return this;
    }
    public String getAddressLine() {
        return this.addressLine;
    }

    public ParseKeywordsResponse setTags(java.util.List<SystemTag> tags) {
        this.tags = tags;
        return this;
    }
    public java.util.List<SystemTag> getTags() {
        return this.tags;
    }

    public ParseKeywordsResponse setTimeRange(ParseTimeRange timeRange) {
        this.timeRange = timeRange;
        return this;
    }
    public ParseTimeRange getTimeRange() {
        return this.timeRange;
    }

}
