<?php

// This file is auto-generated, don't edit it. Thanks.
namespace Aliyun\PDS\SDK\Models;

use AlibabaCloud\Tea\Model;

/**
 * *
 */
class Address extends Model {
    protected $_name = [
        'city' => 'city',
        'country' => 'country',
        'district' => 'district',
        'province' => 'province',
        'township' => 'township',
    ];
    public function validate() {}
    public function toMap() {
        $res = [];
        if (null !== $this->city) {
            $res['city'] = $this->city;
        }
        if (null !== $this->country) {
            $res['country'] = $this->country;
        }
        if (null !== $this->district) {
            $res['district'] = $this->district;
        }
        if (null !== $this->province) {
            $res['province'] = $this->province;
        }
        if (null !== $this->township) {
            $res['township'] = $this->township;
        }
        return $res;
    }
    /**
     * @param array $map
     * @return Address
     */
    public static function fromMap($map = []) {
        $model = new self();
        if(isset($map['city'])){
            $model->city = $map['city'];
        }
        if(isset($map['country'])){
            $model->country = $map['country'];
        }
        if(isset($map['district'])){
            $model->district = $map['district'];
        }
        if(isset($map['province'])){
            $model->province = $map['province'];
        }
        if(isset($map['township'])){
            $model->township = $map['township'];
        }
        return $model;
    }
    /**
     * @var string
     */
    public $city;

    /**
     * @var string
     */
    public $country;

    /**
     * @var string
     */
    public $district;

    /**
     * @var string
     */
    public $province;

    /**
     * @var string
     */
    public $township;

}
