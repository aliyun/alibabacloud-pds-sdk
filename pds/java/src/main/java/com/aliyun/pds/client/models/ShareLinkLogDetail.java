// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * 
 */
public class ShareLinkLogDetail extends TeaModel {
    // expiration
    @NameInMap("expiration")
    public String expiration;

    // has_multi_object
    @NameInMap("has_multi_object")
    public Boolean hasMultiObject;

    // has_pwd
    @NameInMap("has_pwd")
    public Boolean hasPwd;

    // share_id (脱敏)
    @NameInMap("share_id")
    public String shareId;

    // to_parent_path
    @NameInMap("to_parent_path")
    public String toParentPath;

    // to_parent_path_type
    @NameInMap("to_parent_path_type")
    public String toParentPathType;

    // type
    @NameInMap("type")
    public String type;

    public static ShareLinkLogDetail build(java.util.Map<String, ?> map) throws Exception {
        ShareLinkLogDetail self = new ShareLinkLogDetail();
        return TeaModel.build(map, self);
    }

    public ShareLinkLogDetail setExpiration(String expiration) {
        this.expiration = expiration;
        return this;
    }
    public String getExpiration() {
        return this.expiration;
    }

    public ShareLinkLogDetail setHasMultiObject(Boolean hasMultiObject) {
        this.hasMultiObject = hasMultiObject;
        return this;
    }
    public Boolean getHasMultiObject() {
        return this.hasMultiObject;
    }

    public ShareLinkLogDetail setHasPwd(Boolean hasPwd) {
        this.hasPwd = hasPwd;
        return this;
    }
    public Boolean getHasPwd() {
        return this.hasPwd;
    }

    public ShareLinkLogDetail setShareId(String shareId) {
        this.shareId = shareId;
        return this;
    }
    public String getShareId() {
        return this.shareId;
    }

    public ShareLinkLogDetail setToParentPath(String toParentPath) {
        this.toParentPath = toParentPath;
        return this;
    }
    public String getToParentPath() {
        return this.toParentPath;
    }

    public ShareLinkLogDetail setToParentPathType(String toParentPathType) {
        this.toParentPathType = toParentPathType;
        return this;
    }
    public String getToParentPathType() {
        return this.toParentPathType;
    }

    public ShareLinkLogDetail setType(String type) {
        this.type = type;
        return this;
    }
    public String getType() {
        return this.type;
    }

}
