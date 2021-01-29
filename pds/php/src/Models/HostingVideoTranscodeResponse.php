<?php

// This file is auto-generated, don't edit it. Thanks.
namespace Aliyun\PDS\SDK\Models;

use AlibabaCloud\Tea\Model;

/**
 * 转码接口response
 */
class HostingVideoTranscodeResponse extends Model {
    protected $_name = [
        'definitionList' => 'definition_list',
        'duration' => 'duration',
        'hlsTime' => 'hls_time',
    ];
    public function validate() {}
    public function toMap() {
        $res = [];
        if (null !== $this->definitionList) {
            $res['definition_list'] = $this->definitionList;
        }
        if (null !== $this->duration) {
            $res['duration'] = $this->duration;
        }
        if (null !== $this->hlsTime) {
            $res['hls_time'] = $this->hlsTime;
        }
        return $res;
    }
    /**
     * @param array $map
     * @return HostingVideoTranscodeResponse
     */
    public static function fromMap($map = []) {
        $model = new self();
        if(isset($map['definition_list'])){
            if(!empty($map['definition_list'])){
                $model->definitionList = $map['definition_list'];
            }
        }
        if(isset($map['duration'])){
            $model->duration = $map['duration'];
        }
        if(isset($map['hls_time'])){
            $model->hlsTime = $map['hls_time'];
        }
        return $model;
    }
    /**
     * @description definition_list
     * @example 
     * @var string[]
     */
    public $definitionList;

    /**
     * @description duration
     * @example 100
     * @var int
     */
    public $duration;

    /**
     * @description hls_time
     * @example 10
     * @var int
     */
    public $hlsTime;

}
