// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * 
 */
public class RemarksQuery extends TeaModel {
    @NameInMap("IN")
    public java.util.List<String> IN;

    @NameInMap("NOT-IN")
    public java.util.List<String> NOT-IN;

    @NameInMap("NOT-PREFIX")
    public String NOT-PREFIX;

    @NameInMap("PREFIX")
    public String PREFIX;

    public static RemarksQuery build(java.util.Map<String, ?> map) throws Exception {
        RemarksQuery self = new RemarksQuery();
        return TeaModel.build(map, self);
    }

    public RemarksQuery setIN(java.util.List<String> IN) {
        this.IN = IN;
        return this;
    }
    public java.util.List<String> getIN() {
        return this.IN;
    }

    public RemarksQuery setNOT-IN(java.util.List<String> NOT-IN) {
        this.NOT-IN = NOT-IN;
        return this;
    }
    public java.util.List<String> getNOT-IN() {
        return this.NOT-IN;
    }

    public RemarksQuery setNOT-PREFIX(String NOT-PREFIX) {
        this.NOT-PREFIX = NOT-PREFIX;
        return this;
    }
    public String getNOT-PREFIX() {
        return this.NOT-PREFIX;
    }

    public RemarksQuery setPREFIX(String PREFIX) {
        this.PREFIX = PREFIX;
        return this;
    }
    public String getPREFIX() {
        return this.PREFIX;
    }

}
