<?php

// This file is auto-generated, don't edit it. Thanks.

namespace Aliyun\PDS\SDK\Models;

use AlibabaCloud\Tea\Model;

class BaseMediaResponse extends Model
{
    /**
     * @description address_line
     *
     * @example 北京市昌平区白各庄新村路
     *
     * @var string
     */
    public $addressLine;

    /**
     * @description city
     *
     * @example 杭州
     *
     * @var string
     */
    public $city;

    /**
     * @description country
     *
     * @example 中国
     *
     * @var string
     */
    public $country;

    /**
     * @description district
     *
     * @example 余杭区
     *
     * @var string
     */
    public $district;

    /**
     * @description height
     *
     * @example 720
     *
     * @var int
     */
    public $height;

    /**
     * @description location
     *
     * @example 40.110333,116.349311
     *
     * @var string
     */
    public $location;

    /**
     * @description province
     *
     * @example 浙江省
     *
     * @var string
     */
    public $province;

    /**
     * @description time
     *
     * @var string
     */
    public $time;

    /**
     * @description township
     *
     * @example 沙河镇
     *
     * @var string
     */
    public $township;

    /**
     * @description width
     *
     * @example 1024
     *
     * @var int
     */
    public $width;
    protected $_name = [
        'addressLine' => 'address_line',
        'city'        => 'city',
        'country'     => 'country',
        'district'    => 'district',
        'height'      => 'height',
        'location'    => 'location',
        'province'    => 'province',
        'time'        => 'time',
        'township'    => 'township',
        'width'       => 'width',
    ];
    protected $_default = [
        'height' => 0,
        'width'  => 0,
    ];

    public function validate()
    {
    }

    public function toMap()
    {
        $res = [];
        if (null !== $this->addressLine) {
            $res['address_line'] = $this->addressLine;
        }
        if (null !== $this->city) {
            $res['city'] = $this->city;
        }
        if (null !== $this->country) {
            $res['country'] = $this->country;
        }
        if (null !== $this->district) {
            $res['district'] = $this->district;
        }
        if (null !== $this->height) {
            $res['height'] = $this->height;
        }
        if (null !== $this->location) {
            $res['location'] = $this->location;
        }
        if (null !== $this->province) {
            $res['province'] = $this->province;
        }
        if (null !== $this->time) {
            $res['time'] = $this->time;
        }
        if (null !== $this->township) {
            $res['township'] = $this->township;
        }
        if (null !== $this->width) {
            $res['width'] = $this->width;
        }

        return $res;
    }

    /**
     * @param array $map
     *
     * @return BaseMediaResponse
     */
    public static function fromMap($map = [])
    {
        $model = new self();
        if (isset($map['address_line'])) {
            $model->addressLine = $map['address_line'];
        }
        if (isset($map['city'])) {
            $model->city = $map['city'];
        }
        if (isset($map['country'])) {
            $model->country = $map['country'];
        }
        if (isset($map['district'])) {
            $model->district = $map['district'];
        }
        if (isset($map['height'])) {
            $model->height = $map['height'];
        }
        if (isset($map['location'])) {
            $model->location = $map['location'];
        }
        if (isset($map['province'])) {
            $model->province = $map['province'];
        }
        if (isset($map['time'])) {
            $model->time = $map['time'];
        }
        if (isset($map['township'])) {
            $model->township = $map['township'];
        }
        if (isset($map['width'])) {
            $model->width = $map['width'];
        }

        return $model;
    }
}
