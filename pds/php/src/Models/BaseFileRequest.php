<?php

// This file is auto-generated, don't edit it. Thanks.

namespace Aliyun\PDS\SDK\Models;

use AlibabaCloud\Tea\Model;

class BaseFileRequest extends Model
{
    /**
     * @description addition_data
     *
     * @var array
     */
    public $additionData;
    protected $_name = [
        'additionData' => 'addition_data',
    ];

    public function validate()
    {
    }

    public function toMap()
    {
        $res = [];
        if (null !== $this->additionData) {
            $res['addition_data'] = $this->additionData;
        }

        return $res;
    }

    /**
     * @param array $map
     *
     * @return BaseFileRequest
     */
    public static function fromMap($map = [])
    {
        $model = new self();
        if (isset($map['addition_data'])) {
            $model->additionData = $map['addition_data'];
        }

        return $model;
    }
}
