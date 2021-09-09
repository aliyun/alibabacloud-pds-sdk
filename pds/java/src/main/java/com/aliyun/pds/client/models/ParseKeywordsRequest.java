// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * Parse keywords request
 */
public class ParseKeywordsRequest extends TeaModel {
    @NameInMap("httpheaders")
    public java.util.Map<String, String> httpheaders;

    @NameInMap("keywords")
    public String keywords;

    public static ParseKeywordsRequest build(java.util.Map<String, ?> map) throws Exception {
        ParseKeywordsRequest self = new ParseKeywordsRequest();
        return TeaModel.build(map, self);
    }

    public ParseKeywordsRequest setHttpheaders(java.util.Map<String, String> httpheaders) {
        this.httpheaders = httpheaders;
        return this;
    }
    public java.util.Map<String, String> getHttpheaders() {
        return this.httpheaders;
    }

    public ParseKeywordsRequest setKeywords(String keywords) {
        this.keywords = keywords;
        return this;
    }
    public String getKeywords() {
        return this.keywords;
    }

}
