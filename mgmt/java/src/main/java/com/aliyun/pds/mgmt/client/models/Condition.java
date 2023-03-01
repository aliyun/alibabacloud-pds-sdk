// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.mgmt.client.models;

import com.aliyun.tea.*;

/**
 * 
 */
public class Condition extends TeaModel {
    @NameInMap("ip_equals")
    public IPCondition ipEquals;

    @NameInMap("ip_not_equals")
    public IPCondition ipNotEquals;

    @NameInMap("string_like")
    public StringCondition stringLike;

    @NameInMap("string_not_like")
    public StringCondition stringNotLike;

    public static Condition build(java.util.Map<String, ?> map) throws Exception {
        Condition self = new Condition();
        return TeaModel.build(map, self);
    }

    public Condition setIpEquals(IPCondition ipEquals) {
        this.ipEquals = ipEquals;
        return this;
    }
    public IPCondition getIpEquals() {
        return this.ipEquals;
    }

    public Condition setIpNotEquals(IPCondition ipNotEquals) {
        this.ipNotEquals = ipNotEquals;
        return this;
    }
    public IPCondition getIpNotEquals() {
        return this.ipNotEquals;
    }

    public Condition setStringLike(StringCondition stringLike) {
        this.stringLike = stringLike;
        return this;
    }
    public StringCondition getStringLike() {
        return this.stringLike;
    }

    public Condition setStringNotLike(StringCondition stringNotLike) {
        this.stringNotLike = stringNotLike;
        return this;
    }
    public StringCondition getStringNotLike() {
        return this.stringNotLike;
    }

}
