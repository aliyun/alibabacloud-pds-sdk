// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.hosting.mode.models;

import com.aliyun.tea.*;

/**
 * 
 */
public class BaseMediaResponse extends TeaModel {
    // address_line
    @NameInMap("address_line")
    public String addressLine;

    // city
    @NameInMap("city")
    public String city;

    // country
    @NameInMap("country")
    public String country;

    // district
    @NameInMap("district")
    public String district;

    // height
    @NameInMap("height")
    public Long height;

    // system_tags
    @NameInMap("image_tags")
    public java.util.List<SystemTag> imageTags;

    // location
    @NameInMap("location")
    public String location;

    // province
    @NameInMap("province")
    public String province;

    // time
    @NameInMap("time")
    public String time;

    // township
    @NameInMap("township")
    public String township;

    // width
    @NameInMap("width")
    public Long width;

    public static BaseMediaResponse build(java.util.Map<String, ?> map) throws Exception {
        BaseMediaResponse self = new BaseMediaResponse();
        return TeaModel.build(map, self);
    }

    public BaseMediaResponse setAddressLine(String addressLine) {
        this.addressLine = addressLine;
        return this;
    }
    public String getAddressLine() {
        return this.addressLine;
    }

    public BaseMediaResponse setCity(String city) {
        this.city = city;
        return this;
    }
    public String getCity() {
        return this.city;
    }

    public BaseMediaResponse setCountry(String country) {
        this.country = country;
        return this;
    }
    public String getCountry() {
        return this.country;
    }

    public BaseMediaResponse setDistrict(String district) {
        this.district = district;
        return this;
    }
    public String getDistrict() {
        return this.district;
    }

    public BaseMediaResponse setHeight(Long height) {
        this.height = height;
        return this;
    }
    public Long getHeight() {
        return this.height;
    }

    public BaseMediaResponse setImageTags(java.util.List<SystemTag> imageTags) {
        this.imageTags = imageTags;
        return this;
    }
    public java.util.List<SystemTag> getImageTags() {
        return this.imageTags;
    }

    public BaseMediaResponse setLocation(String location) {
        this.location = location;
        return this;
    }
    public String getLocation() {
        return this.location;
    }

    public BaseMediaResponse setProvince(String province) {
        this.province = province;
        return this;
    }
    public String getProvince() {
        return this.province;
    }

    public BaseMediaResponse setTime(String time) {
        this.time = time;
        return this;
    }
    public String getTime() {
        return this.time;
    }

    public BaseMediaResponse setTownship(String township) {
        this.township = township;
        return this;
    }
    public String getTownship() {
        return this.township;
    }

    public BaseMediaResponse setWidth(Long width) {
        this.width = width;
        return this;
    }
    public Long getWidth() {
        return this.width;
    }

}
