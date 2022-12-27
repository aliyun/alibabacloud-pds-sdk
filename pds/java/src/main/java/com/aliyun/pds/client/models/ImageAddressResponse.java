// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * 
 */
public class ImageAddressResponse extends TeaModel {
    @NameInMap("address_detail")
    public Address addressDetail;

    /**
     * <p>聚类地点计数</p>
     */
    @NameInMap("count")
    public Long count;

    /**
     * <p>cover_file_id</p>
     */
    @NameInMap("cover_file_id")
    public String coverFileId;

    /**
     * <p>聚类地点封面图片地址</p>
     */
    @NameInMap("cover_url")
    public String coverUrl;

    /**
     * <p>经纬度</p>
     */
    @NameInMap("location")
    public String location;

    /**
     * <p>聚类地点名称</p>
     */
    @NameInMap("name")
    public String name;

    public static ImageAddressResponse build(java.util.Map<String, ?> map) throws Exception {
        ImageAddressResponse self = new ImageAddressResponse();
        return TeaModel.build(map, self);
    }

    public ImageAddressResponse setAddressDetail(Address addressDetail) {
        this.addressDetail = addressDetail;
        return this;
    }
    public Address getAddressDetail() {
        return this.addressDetail;
    }

    public ImageAddressResponse setCount(Long count) {
        this.count = count;
        return this;
    }
    public Long getCount() {
        return this.count;
    }

    public ImageAddressResponse setCoverFileId(String coverFileId) {
        this.coverFileId = coverFileId;
        return this;
    }
    public String getCoverFileId() {
        return this.coverFileId;
    }

    public ImageAddressResponse setCoverUrl(String coverUrl) {
        this.coverUrl = coverUrl;
        return this;
    }
    public String getCoverUrl() {
        return this.coverUrl;
    }

    public ImageAddressResponse setLocation(String location) {
        this.location = location;
        return this;
    }
    public String getLocation() {
        return this.location;
    }

    public ImageAddressResponse setName(String name) {
        this.name = name;
        return this;
    }
    public String getName() {
        return this.name;
    }

}
