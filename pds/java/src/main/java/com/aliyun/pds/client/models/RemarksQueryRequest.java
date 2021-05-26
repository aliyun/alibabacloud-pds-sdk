// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * 
 */
public class RemarksQueryRequest extends TeaModel {
    @NameInMap("in")
    public java.util.List<String> in;

    @NameInMap("not_in")
    public java.util.List<String> notIn;

    @NameInMap("not_prefix")
    public String notPrefix;

    @NameInMap("prefix")
    public String prefix;

    public static RemarksQueryRequest build(java.util.Map<String, ?> map) throws Exception {
        RemarksQueryRequest self = new RemarksQueryRequest();
        return TeaModel.build(map, self);
    }

    public RemarksQueryRequest setIn(java.util.List<String> in) {
        this.in = in;
        return this;
    }
    public java.util.List<String> getIn() {
        return this.in;
    }

    public RemarksQueryRequest setNotIn(java.util.List<String> notIn) {
        this.notIn = notIn;
        return this;
    }
    public java.util.List<String> getNotIn() {
        return this.notIn;
    }

    public RemarksQueryRequest setNotPrefix(String notPrefix) {
        this.notPrefix = notPrefix;
        return this;
    }
    public String getNotPrefix() {
        return this.notPrefix;
    }

    public RemarksQueryRequest setPrefix(String prefix) {
        this.prefix = prefix;
        return this;
    }
    public String getPrefix() {
        return this.prefix;
    }

}
