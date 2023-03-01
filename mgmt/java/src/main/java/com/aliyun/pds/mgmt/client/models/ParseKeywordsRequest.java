// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.mgmt.client.models;

import com.aliyun.tea.*;

/**
 * Parse keywords request
 */
public class ParseKeywordsRequest extends TeaModel {
    @NameInMap("keywords")
    public String keywords;

    public static ParseKeywordsRequest build(java.util.Map<String, ?> map) throws Exception {
        ParseKeywordsRequest self = new ParseKeywordsRequest();
        return TeaModel.build(map, self);
    }

    public ParseKeywordsRequest setKeywords(String keywords) {
        this.keywords = keywords;
        return this;
    }
    public String getKeywords() {
        return this.keywords;
    }

}
