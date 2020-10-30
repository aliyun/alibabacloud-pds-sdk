<?php

// This file is auto-generated, don't edit it. Thanks.

namespace Aliyun\PDS\SDK\Models;

use AlibabaCloud\Tea\Model;

/**
 * 转码接口response.
 */
class OSSVideoDefinitionResponse extends Model
{
    /**
     * @description definition_list
     *
     * @example
     *
     * @var string[]
     */
    public $definitionList;

    /**
     * @description frame_rate
     *
     * @example 30000/1001
     *
     * @var string
     */
    public $frameRate;
    protected $_name = [
        'definitionList' => 'definition_list',
        'frameRate'      => 'frame_rate',
    ];

    public function validate()
    {
    }

    public function toMap()
    {
        $res = [];
        if (null !== $this->definitionList) {
            $res['definition_list'] = $this->definitionList;
        }
        if (null !== $this->frameRate) {
            $res['frame_rate'] = $this->frameRate;
        }

        return $res;
    }

    /**
     * @param array $map
     *
     * @return OSSVideoDefinitionResponse
     */
    public static function fromMap($map = [])
    {
        $model = new self();
        if (isset($map['definition_list'])) {
            if (!empty($map['definition_list'])) {
                $model->definitionList = $map['definition_list'];
            }
        }
        if (isset($map['frame_rate'])) {
            $model->frameRate = $map['frame_rate'];
        }

        return $model;
    }
}
