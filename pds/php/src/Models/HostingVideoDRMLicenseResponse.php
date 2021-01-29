<?php

// This file is auto-generated, don't edit it. Thanks.
namespace Aliyun\PDS\SDK\Models;

use AlibabaCloud\Tea\Model;

/**
 * DRM License response
 */
class HostingVideoDRMLicenseResponse extends Model {
    protected $_name = [
        'data' => 'data',
        'deviceInfo' => 'device_info',
        'states' => 'states',
    ];
    public function validate() {
        Model::validateRequired('data', $this->data, true);
        Model::validateRequired('deviceInfo', $this->deviceInfo, true);
        Model::validateRequired('states', $this->states, true);
    }
    public function toMap() {
        $res = [];
        if (null !== $this->data) {
            $res['data'] = $this->data;
        }
        if (null !== $this->deviceInfo) {
            $res['device_info'] = $this->deviceInfo;
        }
        if (null !== $this->states) {
            $res['states'] = $this->states;
        }
        return $res;
    }
    /**
     * @param array $map
     * @return HostingVideoDRMLicenseResponse
     */
    public static function fromMap($map = []) {
        $model = new self();
        if(isset($map['data'])){
            $model->data = $map['data'];
        }
        if(isset($map['device_info'])){
            $model->deviceInfo = $map['device_info'];
        }
        if(isset($map['states'])){
            $model->states = $map['states'];
        }
        return $model;
    }
    /**
     * @description drm_data
     * @example xxx
     * @var string
     */
    public $data;

    /**
     * @description device_info
     * @example xxx
     * @var string
     */
    public $deviceInfo;

    /**
     * @description states
     * @example 0
     * @var int
     */
    public $states;

}
