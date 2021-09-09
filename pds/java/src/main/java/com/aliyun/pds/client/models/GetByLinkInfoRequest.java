// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * 
 */
public class GetByLinkInfoRequest extends TeaModel {
    @NameInMap("httpheaders")
    public java.util.Map<String, String> httpheaders;

    // 额外的信息，比如type为mobile时，此字段为国家编号，不填默认86
    @NameInMap("extra")
    public String extra;

    // 唯一身份标识
    @NameInMap("identity")
    @Validation(required = true)
    public String identity;

    // 认证类型
    @NameInMap("type")
    @Validation(required = true)
    public String type;

    public static GetByLinkInfoRequest build(java.util.Map<String, ?> map) throws Exception {
        GetByLinkInfoRequest self = new GetByLinkInfoRequest();
        return TeaModel.build(map, self);
    }

    public GetByLinkInfoRequest setHttpheaders(java.util.Map<String, String> httpheaders) {
        this.httpheaders = httpheaders;
        return this;
    }
    public java.util.Map<String, String> getHttpheaders() {
        return this.httpheaders;
    }

    public GetByLinkInfoRequest setExtra(String extra) {
        this.extra = extra;
        return this;
    }
    public String getExtra() {
        return this.extra;
    }

    public GetByLinkInfoRequest setIdentity(String identity) {
        this.identity = identity;
        return this;
    }
    public String getIdentity() {
        return this.identity;
    }

    public GetByLinkInfoRequest setType(String type) {
        this.type = type;
        return this;
    }
    public String getType() {
        return this.type;
    }

}
